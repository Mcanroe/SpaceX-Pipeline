select * 
from {{ ref('launches') }}
where status_id in (3,4,7) -- all events that are either success or failure
order by launch_dttm_bst desc