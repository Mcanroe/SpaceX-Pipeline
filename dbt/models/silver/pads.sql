{{ config(materialized='table') }}

select
    id as launch_id,
    pad__id as pad_id,
    pad__name as pad_name,
    pad__image__name as pad_image_name,
    pad__image__thumbnail_url as pad_image_thumbnail_url,
    pad__image__credit as pad_image_credit,
    pad__description as pad_description,
    pad__wiki_url as pad_wiki_url,
    pad__map_url as pad_map_url,
    pad__map_image as pad_map_image,
    pad__total_launch_count as pad_total_launch_count,
    pad__latitude as pad_latitude,
    pad__longitude as pad_longitude,
    pad__location__name as pad_location_name,
    pad__location__description as pad_location_description,
    pad__location__map_image as pad_location_map_image,
    pad__location__image__credit as pad_location_image_credit,
from {{ source('bronze', 'launches') }}