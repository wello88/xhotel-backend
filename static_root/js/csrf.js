// Replace 'your_csrf_token' with the actual CSRF token you obtained from cookies
const csrfToken = '4kBdldPUYrRLf87CUNCBt4vkZdQEM3Wpwjbxj9DjmwpEuLq7zhdPjCBvuJrek8iY';

// Example: Make a request with the CSRF token
fetch('/api/some-endpoint/', {
  method: 'Post',  // Or any other HTTP method
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken,
  },
})
  .then(response => response.json())
  .then(data => console.log('Response Data:', data))
  .catch(error => console.error('Error:', error));
