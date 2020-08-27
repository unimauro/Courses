pip install --user google-cloud-bigquery
pip install --user matplotlib

curl -O https://dl.google.com/dl/cloudsdk/channels/
rapid/downloads/google-cloud-sdk-255.0.0-
linux-x86_64.tar.gz
tar zxvf google-cloud-sdk-255.0.0-linux-x86_64.tar.gz
google-cloud-sdk
./google-cloud-sdk/install.sh

gcloud config set project project_name
gcloud auth login
gcloud init
gcloud iam service-accounts create dsdemo
gcloud projects add-iam-policy-binding your_project_id
--member "serviceAccount:dsdemo@your_project_id.iam.
gserviceaccount.com" --role "roles/owner"
gcloud iam service-accounts keys
create dsdemo.json --iam-account
dsdemo@your_project_id.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS=
/home/ec2-user/dsdemo.json


