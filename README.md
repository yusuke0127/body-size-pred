# UNIQLO size recommender
App that recommends clothing sizes that fits the user based on weight, height, age and gender. [Live Demo](https://body-size-pred-frontend-6xm4os3l7a-an.a.run.app/) 
### Size Reference
- [Men sizes](https://image.uniqlo.com/UQ/ST3/jp/imagesother/sizechart/graph_bodysize_uq_m.jpg)
- [Female size](https://image.uniqlo.com/UQ/ST3/jp/imagesother/sizechart/graph_bodysize_uq_w.jpg)

## Code structure
```
├── README.md
├── api
│   ├── Dockerfile
│   ├── main.py
│   ├── models
│   ├── requirements.txt
│   ├── test
│   └── utils
├── cloudbuild.yml
├── data
├── docker-compose.yml
├── models
├── notebooks
├── predictions
└── streamlit
    ├── Dockerfile
    ├── main.py
    └── requirements.txt
```

- <code>api</code> Directory where the FastAPI code is and its associated Dockerfile.
- <code>data</code> Directory that includes the data used for model training and testing.
- <code>streamlit</code> Directory for the frontend code.
- <code>notebooks</code> Directory where the notebook used for developing the model and other utils used for custom transformations and some feature engineering.
- <code>cloudbuild.yml</code> Config file to implement continuous deployment using Google Cloud Build


## Local development
Uncomment and comment out the lines shown below:
```Docker
# /streamlit/Dockerfile
# Use the lines below when developing locally
EXPOSE 8501

CMD ["streamlit", "run", "main.py"]

# When deploying to GCP
CMD streamlit run --server.port $PORT main.py
```

```Docker
# /api/Dockerfile
# Use this when running locally
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

# Use this when deploying to GCP
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
```

Then build the images by running: `docker compose up -d --build` and run `docker compose up` to start the service instances

## App deployment
This application is structured to be run and to be deployed on Google Cloud Platform using Cloud build to create two separate images of the api and the streamlit and deploy these images to each own separate services.

### GCP setup
1. Create a GCP billing account
2. Enable Cloud Run, Artifact Registry, Cloud Run and Cloud build
3. Connect Cloud Build to a GitHub repository to set up a trigger when the `main` branch is updated.
4. Once the build has started and completed successfully, you can find your images in Artifact Registry on GCP.

Every merge to `main` gets auto deployed to Cloud Run but to deploy manually follow the steps below:

### Manual deployment
1. Make sure to move to the specific directory or service that you're working on. If working on the backend, move to `/api` first before runnig the commands below.
1. Set the env vars to use
```bash
DOCKER_REPO_NAME="your-repo-name"
GCP_REGION="region" # Ex. us-central1
GCP_PROJECT_ID="your-project-id"
DOCKER_IMAGE_NAME="your-docker-image-name"
```
2. Check the env vars
```bash
echo $GCP_REGION
echo $GCP_PROJECT_ID
echo $DOCKER_REPO_NAME
echo $DOCKER_IMAGE_NAME
```
3. Test build locally:
```bash
docker build -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME:0.1 .
```
4. To check the built image: `docker images`
5. To run the instances locally:
```bash
docker run -e PORT=8000 -p 8080:8000 $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME:0.1
```
6. If working on M# machines, make sure to build a linux specific image by using `--platform` flag
```bash
docker build --platform linux/amd64 -t $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME:0.1 .
```
7. Pushing the image to Artifact Registry:
```bash
docker push $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME:0.1
```
8. Deploying to Cloud Run:
```bash
gcloud run deploy --image $GCP_REGION-docker.pkg.dev/$GCP_PROJECT_ID/$DOCKER_REPO_NAME/$DOCKER_IMAGE_NAME:0.1 --region $GCP_REGION
```
9. Stopping Cloud Run instances:
```
gcloud run services list
gcloud run services delete <SERVICE_NAME>
```