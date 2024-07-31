<h1> DataPipeline_doge-thb </h1> 
<p align="center">
  <img src="./pics/doge_00.png" width="1000"> <br>
  data pipeline overview
</p>

<h3> 1) Create dataset and table in BigQuery </h3> 
<p>
  <img src="./pics/doge_01.png" width="400" height="450"> 
  <img src="./pics/doge_02.png" width="400" height="450"> <br>
  <img src="./pics/doge_03.png" width="600"> <br>
  <p> create the dataset and table successfully </p>
</p>

<h3> 2) Create a function in Cloud Functions </h3>
<p>
  <img src="./pics/doge_04.png" width="400"> 
  <img src="./pics/doge_05.png" width="400"> <br>
  <p> set the trigger type is Cloud Pub/Sub, create the topic and then set up the environment variables </p> <br>
  <img src="./pics/doge_06.png" width="700"> 
  <p> add code </p>
</p>

<h3> 3) Create job in Cloud Scheduler </h3>
<p>
  <img src="./pics/doge_07.png" width="400">
  <img src="./pics/doge_08.png" width="400"> <br>
  <p> set the schedule to have Cloud Pub/Sub execute every 5 minutes </p>
</p>

<h3> 4) Check data in BigQuery and create view </h3>
<p>
  <img src="./pics/doge_09.png" width="600"> <br>
  <p> data has been successfully loaded into BigQuery </p> <br>
  <img src="./pics/doge_10.png" width="600"> 
  <p> create view  </p> <br>
  <img src="./pics/doge_11.png" width="600"> 
  <p> create view successfully </p>
</p>

<h3> 5) Create a dashboard in BigQuery using a view as the data source </h3>
<p>
  <img src="./pics/doge_12.png" width="700"> <br>
  <p> DOGE_THB dashboard 🐶</p>
  >>
  <a href="https://lookerstudio.google.com/reporting/7189bc3a-2d1a-4915-8011-08cbf65969a5"> LINK to Dashboard </a>
  ✌️
</p>

<h2> Reference </h2>
<p>
  <ul>
    <li> <a href="https://github.com/fonylew/simple-cloud-functions-to-bigquery"> https://github.com/fonylew/simple-cloud-functions-to-bigquery </a> </li>
    <li> <a href="https://github.com/bitkub/bitkub-official-api-docs"> https://github.com/bitkub/bitkub-official-api-docs </a> </li>
  </ul>
</p>
