import os
from supabase import create_client, Client
from dotenv import load_dotenv
from dataclasses import dataclass, field
from datetime import datetime

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")
supabase = create_client(url, key)

TABLE = "library"
schema = {
    '_id': '',
    'title': '',
    'director': '',
    'year': None,
    'cast': '',
    'series': '',
    'tags': '',
    'last_watched': '',
    'rating': None,
    'description': '',
    'video_link': '',
}

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list)
    series: list[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0
    tags: list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None

# def create_supa(
#     title="", 
#     director="", 
#     year=None,
#     cast='',
#     series='',
#     tags='',
#     last_watched='',
#     rating=None,
#     description='',
#     video_link=''
#     ):
    
#     table = TABLE
#     SCHEMA = {
#         'title': title,
#         'director': director,
#         'year': year,
#         'cast': cast,
#         'series': series,
#         'tags': tags,
#         'last_watched': last_watched,
#         'rating': rating,
#         'description': description,
#         'video_link': video_link,
#     }
    
#     data = supabase.table(table).insert(SCHEMA).execute()
#     ### OR data = supabase.table("TABLE").insert({"name":"Germany"}).execute()

#     return data.data

def create_supa(schema):
    
    table = TABLE
    
    data = supabase.table(table).insert(schema).execute()
    ### OR data = supabase.table("TABLE").insert({"name":"Germany"}).execute()

    return data.data


def read_supa():
    table = TABLE
    data = supabase.table(table).select('*').execute()
    
    return data.data

def select_from_id(_mid):
    table = TABLE
    data = supabase.table(table).select("_id").eq(_mid).execute()
    
    return data.data

def update_supa(id:int, 
                title="", 
                director="", 
                year=None,
                cast='',
                series='',
                tags='',
                last_watched='',
                rating=None,
                description='',
                video_link=''
                ):
    
    table = TABLE
    SCHEMA = {
        'title': title,
        'director': director,
        'year': year,
        'cast': cast,
        'series': series,
        'tags': tags,
        'last_watched': last_watched,
        'rating': rating,
        'description': description,
        'video_link': video_link,
    }
    
    data = supabase.table(table).update(SCHEMA).eq("id", id).execute()
    return data.data

def delete_supa(id: int):
    table = TABLE
    
    data = supabase.table(table).delete().eq("id", id).execute()
    return data.data

