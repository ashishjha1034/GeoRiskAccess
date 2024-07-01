document.getElementById('calculate-btn').addEventListener('click', function() {
    fetch('/calculate_risk', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('epi-value').textContent = data.epi;
        document.getElementById('udi-value').textContent = data.udi;
        document.getElementById('luv-value').textContent = data.luv;
        document.getElementById('cri-value').textContent = data.cri;
        document.getElementById('risk-factor-value').textContent = data.risk_factor;
        document.getElementById('risk-classification-value').textContent = data.predicted_cluster;

        // Add this line to display the generated text in the new div
    })
    .catch(error => console.error('Error:', error));

    document.querySelector('.home-icon').addEventListener('click', function() {
    window.location.href = '/';
    });
});
