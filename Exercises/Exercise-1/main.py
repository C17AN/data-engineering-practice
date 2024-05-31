import requests
import zipfile
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

# 파일을 다운로드 한다
# 저장할 파일명을 정한다
# 저장한다

def download(download_target):
    for url in download_uris:
        try: 
            response = requests.get(url)
            response.raise_for_status()
            filename = url.split("/")[-1]
            path = os.path.join(download_target, filename)
            print(path)
            with open(path, 'wb') as file:
                file.write(response.content)
                
            if filename.endswith('zip'):
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    unzip_path = os.path.join(download_target, filename.replace('.zip', ''))
                    print(f"Unzipping to {unzip_path}")
                    zip_ref.extractall(unzip_path)
                    os.remove(path)
        except requests.ConnectTimeout:
            print("타임아웃이 발생했습니다.")
        except Exception as e:
            print(f"오류가 발생했습니다. : {e}")
                
        
        
        

def main():
    download_target = "downloads"
    if(not os.path.isdir(download_target)):
        os.mkdir(download_target)
    download(download_target)
    # your code here
    
    pass


if __name__ == "__main__":
    main()
