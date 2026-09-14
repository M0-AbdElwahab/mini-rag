from enum import Enum

class ResponseSignal(Enum):

    FILE_TYPE_INVALID = "Invalid file type"
    FILE_SIZE_EXCEEDED = "File size exceeds the limit"  
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_VALIDATION_SUCCESS = "File Validation successful"
    FILE_PROCESSING_FAILED = "File processing failed"
    FILE_PROCESSING_SUCCESS = "File processing successful"