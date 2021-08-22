echo "Generating deploy file for backend"

gcpFirebaseProjectId=$1

sed -i "s/gcp_firebase_project_id/$gcpFirebaseProjectId/" ./backend/app.yaml