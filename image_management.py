from cloudinary import uploader, CloudinaryImage
  
def upload(file_name, user_id):
    response = uploader.upload(file_name, tags=user_id)
    return response['secure_url'], response['public_id']

def getPreviewImage(imageId):
    return CloudinaryImage(imageId).build_url(width=240).replace("p:/","ps:/")
