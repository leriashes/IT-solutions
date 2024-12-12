from django.core.management.base import BaseCommand
from reviews.models import Review
import requests

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        url = 'https://public-api.reviews.2gis.com/2.0/branches/70000001080371174/reviews?limit=50&is_advertiser=true&fields=meta.branch_rating,meta.branch_reviews_count,meta.total_count&without_my_first_review=false&rated=true&sort_by=date_edited&key=37c04fe6-a560-4549-b459-02309cf643ad&locale=ru_RU'
        self.get_reviews(url)

    def fetch_reviews(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"API request failed with status {response.status_code}: {response.text}")

    def save_reviews(self, data):
        for review in data.get('reviews', []):
            Review.objects.update_or_create(
                author_name=review.get('user', {}).get('first_name', 'Аноним'),
                date_created=review.get('date_created'),
                defaults={
                    'text': review.get('text', ''),
                    'rating': review.get('rating', 0),
                    'author_photo': review.get('user').get('photo_preview_urls').get('640x')
                }
            )

    def get_reviews(self, url):
        while url is not None:
            try:
                print('\n\n', url)
                data = self.fetch_reviews(url)
            
                print('\n', data)
                url = data.get('meta').get('next_link')

                if not data['reviews']:
                    print(f"No more reviews. Stopping.")
                    break

                self.save_reviews(data)

            except Exception as e:
                print(f"Error: {e}")
                break
        