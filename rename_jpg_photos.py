import piexif
from datetime import datetime
import os,glob



# directory format : dir = r"x:\YOUR PHOTO DIRECTORY"
def rename_photos_by_date(photo_dir):
    list = os.listdir(photo_dir)
    filetype = glob.glob(photo_dir+r"\*.jpg")

    file_name_set = set()
    if len(filetype) !=0:
        for i in filetype:
            image = piexif.load(i)
            exif = image["Exif"]
            date_ori = exif[piexif.ExifIFD.DateTimeOriginal].decode('utf-8')
            date_obj = datetime.strptime(date_ori, "%Y:%m:%d %H:%M:%S")
            file_name = i.split('\\')[-1]

            # new name
            file_number = "01"
            to_file_name = str(date_obj.date())+" "+file_number
            while to_file_name in file_name_set:
                if int(file_number)>=9:
                    file_number = str(int(file_number)+1)
                else:
                    file_number = "0"+str(int(file_number)+1)
                to_file_name = str(date_obj.date())+" "+file_number
            os.rename(i,photo_dir+"\\"+to_file_name+".jpg")
            file_name_set.add(to_file_name)

            print(file_name,"to",to_file_name+".jpg")




