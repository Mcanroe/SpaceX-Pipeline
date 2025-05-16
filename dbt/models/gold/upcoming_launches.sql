select * 
from {{ ref('launches') }}
where status_id not in (3,4,7) -- all events that are not success or failure , includes events that are TBC, TBD , etc.
order by launch_dttm_bst