# Install

##### Requirements
確認済動作環境: Ubuntu18,python3.8

### 環境構築
## 1. 依存ライブラリのインストール
```
sudo apt install -y build-essential  libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev tk-dev  
sudo apt install -y curl wget  git default-jre
```
## 2.  pyenv と python 3.8 のインストール
python 3.8環境を導入するためにここではpyenvを紹介しますが、他の方法でも問題ありません。

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

##### install and activate specific version python
````
pyenv install 3.8.13
````
````
# 3.8.13をシステム全体で使いたい場合は global　optionを使う
pyenv global 3.8.13

# 3.8.13を特定のディレクトリ内だけで使いたい場合は、環境を使用したいディレクトリ内で local optionを使う
pyenv local 3.8.13

python -V
pip install --upgrade pip
````

## 3.  CityGMLtoRobotMap　のインストール 
#### Clone CityGMLtoRobotMap
````
git clone https://github.com/sensyn-robotics/PLATEAU-UC22-024-CityGMLtoRobotMap CityGMLtoRobotMap
cd ./CityGMLtoRobotMap
````

#### Download [citygml-tools](https://github.com/citygml4j/citygml-tools)
````
wget --content-disposition https://github.com/citygml4j/citygml-tools/releases/download/v2.0.0/citygml-tools-2.0.0.zip
unzip citygml-tools-2.0.0.zip
````

#### Download [IfcConverter](https://blenderbim.org/docs-python/ifcconvert/installation.html) （BIMを使う場合）
````
# operation checked on only ubuntu18 
wget --content-disposition https://s3.amazonaws.com/ifcopenshell-builds/IfcConvert-v0.6.0-0087fa8-linux64.zip
unzip IfcConvert-*-linux64.zip
````

####  CityGMLtoRobotMap が必要とする　python dependency のインストール

````
pip install poetry
poetry install
# swich into poetry environment
poetry shell
````
   



