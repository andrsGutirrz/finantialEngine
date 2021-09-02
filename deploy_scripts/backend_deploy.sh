echo "Generating deploy file for backend"

gcpFirebaseProjectId=$1
echo $gcpFirebaseProjectId
sed -i "s/gcp_firebase_project_id/$gcpFirebaseProjectId/" ./backend/app.yaml

cat ./backend/app.yaml