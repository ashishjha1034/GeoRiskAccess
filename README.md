# GIS-RISK-FACTOR (GeoRiskAccess)

GeoRiskAccess is a comprehensive project that leverages Geographic Information Systems (GIS) to analyze pollution and risk factors in urban environments, with a focus on Pune, India, particularly the Katraj area.

## Project Overview

GeoRiskAccess integrates real-time sensor data from various environmental monitoring devices to provide insights into urban environmental conditions and associated risks. The project aims to create a web-based platform for informed decision-making in urban planning, disaster management, and public health interventions.

## Key Features

- Real-time data collection from multiple sensor types
- GIS-based analysis of environmental and urban factors
- Web-based platform for data visualization and risk assessment
- Focus on Pune, India, with emphasis on the Katraj area

## Data Sources

The project incorporates data from various sources, including:

- DHT-11 sensors (temperature and humidity)
- MQ-135 sensors (air quality)
- RTC modules (real-time clock)
- SD card modules (data storage)
- PM2.5 GP2Y1010AU0F optical dust sensor modules

## Analyzed Factors

GeoRiskAccess analyzes several factors to assess environmental conditions and risks:

- Population density
- Locations of fire stations, police stations, and parks
- Air quality (PM2.5 and other pollutants)
- Traffic density
- Land use patterns
- Weather conditions
- Topography
- Nighttime Lights (NTL) for economic activity
- Normalized Difference Vegetation Index (NDVI) for vegetation cover

  #Clone and run requirement.txt
  pip install -r requirement.txt

## Platform Functionality

Users can:

- Select specific locations within Pune (focusing on Katraj area)
- Access visualizations of environmental data
- Obtain risk factor assessments based on a trained model

## Project Goals

- Provide valuable insights into urban environmental conditions
- Facilitate informed decision-making for urban planning and management
- Contribute to sustainable development and urban resilience
- Enable effective addressing of pollution and risk factors in urban areas

## Repository Structure

<pre>
<code>
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
</code>
</pre>

