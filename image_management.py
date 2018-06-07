from cloudinary import uploader, CloudinaryImage
  
def upload(user_name, file_name):
    response = uploader.upload(file_name, tags=user_name)
    return response['secure_url'], response['public_id']

def getPreviewImage(imageId):
    return CloudinaryImage(imageId).build_url(width=240).replace("p:/","ps:/")
