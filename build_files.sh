python3 pip install --upgrade pip setuptools
sudo apt install libsqlite3-dev
pyenv install 3.9

echo "Building project packages..."
cd taxiapp
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput