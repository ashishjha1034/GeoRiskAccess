<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>GeoRiskAccess: GIS-Based Urban Environmental Risk Analysis</h1>

  <p>
        <img src="https://img.shields.io/github/contributors/ashishjha1034/GeoRiskAccess.svg?style=for-the-badge" alt="Contributors">
        <img src="https://img.shields.io/github/forks/ashishjha1034/GeoRiskAccess.svg?style=for-the-badge" alt="Forks">
    </p>

  <h2>About The Project</h2>

  <p>GeoRiskAccess is a comprehensive project that leverages Geographic Information Systems (GIS) to analyze pollution and risk factors in urban environments, with a focus on Pune, India, particularly the Katraj area.</p>

  <h2>Project Overview</h2>

  <p>GeoRiskAccess integrates real-time sensor data from various environmental monitoring devices to provide insights into urban environmental conditions and associated risks. The project aims to create a web-based platform for informed decision-making in urban planning, disaster management, and public health interventions.</p>

  <h2>Key Features</h2>
    <ul>
        <li>Real-time data collection from multiple sensor types</li>
        <li>GIS-based analysis of environmental and urban factors</li>
        <li>Web-based platform for data visualization and risk assessment</li>
        <li>Focus on Pune, India, with emphasis on the Katraj area</li>
    </ul>

  <h2>Data Sources</h2>
    <p>The project incorporates data from various sources, including:</p>
    <ul>
        <li>DHT-11 sensors (temperature and humidity)</li>
        <li>MQ-135 sensors (air quality)</li>
        <li>RTC modules (real-time clock)</li>
        <li>SD card modules (data storage)</li>
        <li>PM2.5 GP2Y1010AU0F optical dust sensor modules</li>
    </ul>

  <h2>Analyzed Factors</h2>
    <p>GeoRiskAccess analyzes several factors to assess environmental conditions and risks:</p>
    <ul>
        <li>Population density</li>
        <li>Locations of fire stations, police stations, and parks</li>
        <li>Air quality (PM2.5 and other pollutants)</li>
        <li>Traffic density</li>
        <li>Land use patterns</li>
        <li>Weather conditions</li>
        <li>Topography</li>
        <li>Nighttime Lights (NTL) for economic activity</li>
        <li>Normalized Difference Vegetation Index (NDVI) for vegetation cover</li>
    </ul>
    

 <h2>Installation</h2>
    <h3>1. Fork</h3>
    <pre><code>git clone https://github.com/ashishjha1034/GeoRiskAccess.git</code></pre>

  <h3>2. Navigate to the project directory</h3>
    <pre><code>cd GeoRiskAccess</code></pre>

  <h3>3. Install Requirements</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

  <h2>Platform Functionality</h2>
    <p>Users can:</p>
    <ul>
        <li>Select specific locations within Pune (focusing on Katraj area)</li>
        <li>Access visualizations of environmental data</li>
        <li>Obtain risk factor assessments based on a trained model</li>
    </ul>

   <h2>Project Goals</h2>
    <ul>
        <li>Provide valuable insights into urban environmental conditions</li>
        <li>Facilitate informed decision-making for urban planning and management</li>
        <li>Contribute to sustainable development and urban resilience</li>
        <li>Enable effective addressing of pollution and risk factors in urban areas</li>
    </ul>

  <h2>Repository Structure</h2>
    <pre><code>
├── .idea
├── Lib/site-packages
├── Scripts
├── static
├── templates
├── .gitattributes
├── NTL_Katraj (1).csv
├── RISKK.csv
├── main_indices.csv
├── mainapp.py
├── ndvi_katraj_time.csv
├── new.py
├── practise.csv
├── practise.xlsm
├── practisef.csv
├── pyvenv.cfg
    </code></pre>

  <h2>Images</h2>
    <img src="https://github.com/user-attachments/assets/89e6a131-5cdb-4d07-ab47-e68b24a69506" alt="Screenshot 1">
    <img src="https://github.com/user-attachments/assets/61a8ecb8-d120-48b6-9d3b-ac62e5c0b113" alt="Screenshot 2">
    <img src="https://github.com/user-attachments/assets/09f027de-895a-42fd-b383-470dda9a1999" alt="Screenshot 3">

</body>
</html>
