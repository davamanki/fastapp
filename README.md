# fastapp
Simple FastAPI + PostgreSQL app with docker-compose (for learning purposes).

How to Use:
Rename ".env.example" to ".env" and change data to connect your PostgreSQL database:
POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

Download to server:

P.S. You can rule your server from CMD. Connect with
<pre>ssh root@ServerIp</pre>

### **GitHub**

<pre>sudo apt-get update</pre>
<pre>sudo apt-get install git</pre>

### **DOCKER**
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
<pre># Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update</pre>

<pre>sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin</pre>

### Clone Git
<pre>git clone https://github.com/davamanki/fastapp.git</pre>

### Move to "fastapp"
<pre>cd fastapp</pre>
#### **Build Docker-Compose**
<pre>docker compose build</pre>
<pre>docker compuse up -d</pre>

App is working!
Docs at `ServerId:8000/docs`