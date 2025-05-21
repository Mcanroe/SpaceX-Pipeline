select distinct
    pad_name,
    pad_total_launch_count,
    pad_map_image,
    pad_wiki_url
from {{ ref('pads') }}
where pad_total_launch_count <> 0