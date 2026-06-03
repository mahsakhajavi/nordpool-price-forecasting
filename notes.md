## Project notes

Got ENTSO-E working — NO1 day-ahead prices come in 15-min resolution (EUR/MWh).
Next: pull longer range → save to CSV → resample to hourly → add Open-Meteo temp.

3-month price data crosses the March daylight-saving change → timestamps had mixed 
+01:00/+02:00 offsets → fixed with pd.to_datetime(..., utc=True).