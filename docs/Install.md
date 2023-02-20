# Install

##### Requirements
確認済動作環境: Ubuntu18,python3.8

### 環境構築
### 1. install dependency library
```
sudo apt install -y build-essential  libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev tk-dev  
sudo apt install -y curl wget  git default-jre
```
### 2. install pyenv and python 3.8 

##### download pyenv
````
curl https://pyenv.run | bash
````

##### set envirnment values and activate pyenv
````
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
````

##### install specific version python
````
pyenv install 3.8.13
pyenv global 3.8.13
pip install --upgrade pip
````


## CityGMLtoRobotMap インストール方法 
#### Clone CityGMLtoRobotMap
````
git clone https://github.com/sensyn-robotics/PLATEAU-UC22-024-CityGMLtoRobotMap CityGMLtoRobotMap
cd ./CityGMLtoRobotMap
````
TODO : self url 

#### Download [citygml-tools](https://github.com/citygml4j/citygml-tools)
````
wget --content-disposition https://github.com/citygml4j/citygml-tools/releases/download/v2.0.0/citygml-tools-2.0.0.zip
unzip citygml-tools-2.0.0.zip
````

#### Download [IfcConverter](https://blenderbim.org/docs-python/ifcconvert/installation.html) （BIMを使う場合）
````
wget --content-disposition https://s3.amazonaws.com/ifcopenshell-builds/IfcConvert-v0.7.0-07ee62e-linux64.zip
unzip IfcConvert-*-linux64.zip
````

#### install CityGMLtoRobotMap python dependency 
````
pyenv global 3.8.13

pyenv local 3.8.13

pip install --upgrade pip
````
````
pip install poetry
poetry install
# swich into poetry environment
poetry shell
````
   



