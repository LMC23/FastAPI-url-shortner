from supabase import create_client, Client
from settings import settings

client: Client = create_client(settings.project_url, settings.service_role_secret)
# test = client.table("url_table").select("*").execute()
# print(test)
