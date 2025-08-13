from pars_hitmotop import RatingPage, RatingCount, EnteredTrack
import uvicorn
from datetime import datetime
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from typing import Union, List, Optional, Dict

app = FastAPI()



class Track(BaseModel):
    author: str
    title: str
    url_down: str
    direct_download_link: Union[str, None]
    duration_track: str
    picture_url: str
    url_track: str

class Tracks(BaseModel):
    time_spent: str
    data: List[Track]


@app.get('/rating_track', summary='Рейтинговые треки', tags=['Рейтинговые треки'])
async def rating_count(count: int, direct_link:bool=False)-> Tracks:
    start = datetime.now()
    try:
        res = RatingCount(count, direct_link).data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {'time_spent':str((datetime.now()-start).total_seconds()), "data":res}
    
@app.get('/rating_page', summary='Рейтинговые страницы', tags=['Рейтинговые треки'])
async def rating_page(page: int, direct_link:bool=False) -> Tracks:
    start = datetime.now()
    try:
        res = RatingPage(page, direct_link).data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    else:
        return {'time_spent':str((datetime.now()-start).total_seconds()), "data":res}
    
    


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)