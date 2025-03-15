import axios from 'axios';

// Base configuration for Axios
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com', // Replace with your API URL
  timeout: 5000, // Timeout limit for requests
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to fetch data from API
export const fetchPosts = async () => {
  try {
    const response = await apiClient.get('/posts');
    return response.data;
  } catch (error) {
    console.error('Error fetching posts:', error);
    throw error;
  }
};
