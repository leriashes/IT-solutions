document.addEventListener('DOMContentLoaded', function() {
    var phoneElement = document.getElementById('id_phone');
    var phoneMask = IMask(phoneElement, {
        mask: '+{7} (000) 000-00-00'
    });
});
