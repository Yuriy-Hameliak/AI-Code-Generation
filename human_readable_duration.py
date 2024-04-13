def format_duration(seconds):
  """
  Formats a given number of seconds into a human-readable string representation of the duration.

  Args:
      seconds: The number of seconds to format.

  Returns:
      A string representing the formatted duration.
  """
  if seconds == 0:
    return "now"

  units = [("year", 31536000), ("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
  parts = []
  for unit, div in units:
    value = seconds // div
    if value > 0:
      plural = "s" if value > 1 else ""
      parts.append(f"{value} {unit}{plural}")
      seconds -= value * div
  return ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1]
