document.addEventListener("DOMContentLoaded", function() {
    fetch('/calculate_indices')
        .then(response => response.json())
        .then(data => {
            document.getElementById('co-image').querySelector('.value').innerText = data.b_co_avg;
            document.getElementById('so2-image').querySelector('.value').innerText = data.c_so2_avg;
            document.getElementById('dust-image').querySelector('.value').innerText = data.d_aod_avg;
            document.getElementById('temp-image').querySelector('.value').innerText = data.temperature_avg;
            document.getElementById('humidity-image').querySelector('.value').innerText = data.humidity_avg;
            document.getElementById('ntl-image').querySelector('.value').innerText = data.ntl_avg;
        });

    document.getElementById('nextButton').addEventListener('click', function() {
        window.location.href = '/risk';  // Replace with your actual next page URL
    });
    document.querySelector('.home-btn').addEventListener('click', function() {
    window.location.href = '/';
    });

});
