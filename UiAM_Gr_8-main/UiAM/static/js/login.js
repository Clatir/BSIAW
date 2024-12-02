function aktualizujPole() {
    var pole = document.getElementById('fa_code');
    var val = pole.value.replace(/[^0-9\b]/g, ''); // Usuń wszystko, co nie jest cyfrą
    var currentPosition = pole.selectionStart;    

    // Wypełnij pozostałe miejsca literami 'n'
    while (val.length < 6) {
        val += 'n';
    }
    // Ustaw wartość z powrotem na pole formularza, ograniczając do 6 znaków
    pole.value = val.substring(0, 6);


    pole.setSelectionRange(currentPosition, currentPosition);


}

