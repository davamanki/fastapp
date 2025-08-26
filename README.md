# fastapp
Simple FastAPI + PostgreSQL app with docker-compose (for learning purposes).

## How to Use
1. Rename `.env.example` to `.env` and set values for:
```
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
APP_PORT=8000
DATABASE_URL=postgresql+asyncpg://your_user:your_password@db:5432/tasks
```

2. Connect to your server: `ssh root@ServerIp` (or continue in web server console)

### **Install Git**
```
sudo apt-get update
sudo apt-get install git
```

### **Install Docker**

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Clone Git Project
```
git clone https://github.com/davamanki/fastapp.git
cd fastapp
```

#### **Run App**
```
docker compose build
docker compose up -d
```

App is working! 🚀

Docs available at:```ServerId:8000/docs```