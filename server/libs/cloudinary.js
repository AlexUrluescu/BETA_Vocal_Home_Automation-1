import {v2 as cloudinary} from 'cloudinary';

cloudinary.config({
    cloud_name: "dmbtukbak",
    api_key: "964269477483283",
    api_secret: "Spv56xoqsEeDUKY7c_urePg7924"
})

export const uploadImage = async filePath => {
    return await cloudinary.uploader.upload(filePath, {
        folder: "folder_images"
    })
}

export const deleteImage = async id => {
    return await cloudinary.uploader.destroy(id)
}