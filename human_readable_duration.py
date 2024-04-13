def format_duration(seconds):
  """
  Formats a duration in seconds as a human-readable string.

  Args:
      seconds: A non-negative integer representing the duration in seconds.

  Returns:
      A string representing the human-friendly duration format.
  """
  if seconds == 0:
    return "now"

  units = [("year", 365 * 24 * 60 * 60),
           ("day", 24 * 60 * 60),
           ("hour", 60 * 60),
           ("minute", 60),
           ("second", 1)]
  components = []
  for unit, value in units:
    amount, remainder = divmod(seconds, value)
    if amount > 0:
      components.append(f"{amount} {unit}{'s' if amount > 1 else ''}")
      seconds = remainder
  return ", ".join(components[:-1]) + " and " + components[-1] if len(components) > 1 else components[0]
