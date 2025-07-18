document.getElementById('generateButton').addEventListener('click', async () => {
  const length = parseInt(document.getElementById('length').value);
  const includeUpper = document.getElementById('includeUpper').checked;
  const includeLower = document.getElementById('includeLower').checked;
  const includeNumbers = document.getElementById('includeNumbers').checked;
  const includeSymbols = document.getElementById('includeSymbols').checked;

  const response = await fetch('/generate-password', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      length,
      include_upper: includeUpper,
      include_lower: includeLower,
      include_numbers: includeNumbers,
      include_symbols: includeSymbols
    })
  });

  const data = await response.json();
  if (!response.ok) {
  document.getElementById('passwordValue').textContent = data.error;
} else {
  document.getElementById('passwordValue').textContent = data.password;
});
