# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/

class Solution(object):
    def earliestFinishTime(self, land_start_times: List[int], land_durations: List[int], water_start_times: List[int], water_durations: List[int]) -> int:
        shortest_time_found = 3000

        for land_index in range(len(land_start_times)):
            for water_index in range(len(water_start_times)):
                total_time = land_start_times[land_index] + land_durations[land_index] + water_durations[water_index]
                if land_start_times[land_index] + land_durations[land_index] < water_start_times[water_index]:
                    total_time += water_start_times[water_index] - (land_start_times[land_index] + land_durations[land_index])
                shortest_time_found = total_time if total_time < shortest_time_found else shortest_time_found
        
        for water_index in range(len(water_start_times)):
            for land_index in range(len(land_start_times)):
                total_time = water_start_times[water_index] + water_durations[water_index] + land_durations[land_index]
                if water_start_times[water_index] + water_durations[water_index] < land_start_times[land_index]:
                    total_time += land_start_times[land_index] - (water_start_times[water_index] + water_durations[water_index])
                shortest_time_found = total_time if total_time < shortest_time_found else shortest_time_found

        return shortest_time_found