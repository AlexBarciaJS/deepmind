from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

# Connect to MongoDB using async driver
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
collection = db["scanned_sites"]
pdf_collection = db["scanned_files"]

async def get_scan_record(site):
    """Retrieves the scan log for a given site."""
    return await collection.find_one({"source": site})

async def insert_scan_record(record):
    """Insert a new scan record."""
    await collection.insert_one(record)

async def update_scan_record(site, update_data):
    """Updates a site record with the data provided."""
    await collection.update_one({"source": site}, {"$set": update_data})

async def check_pdf_exists(file_name, file_size, creation_date, modification_date):
    """
    Check if a PDF file has been processed before, based on its file_name, file_size, creation_date, and modification_date.
    Returns True if a record exists, otherwise False.
    """
    query = {
        "file_name": file_name,  # Correct field name
        "file_size": file_size,  # Correct field name
        "creation_date": creation_date,  # Correct field name
        "modification_date": modification_date  # Correct field name
    }

    # Debugging: Print query and all records
    existing_records = await pdf_collection.find().to_list(length=10)
    print(f"Existing records in MongoDB: {existing_records}")

    print(f"Checking if PDF exists with corrected query: {query}")

    result = await pdf_collection.find_one(query)

    print(f"Query result: {result}")

    return result is not None  # Return True/False


async def insert_pdf_record(record):
    """
    Insert a PDF metadata record into MongoDB and return the inserted document ID.
    """
    result = await pdf_collection.insert_one(record)  # Ensure this is awaited
    return str(result.inserted_id)  # Convert ObjectId to string
