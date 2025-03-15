import axios from 'axios';

// Load environment variables
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const API_QUESTION_URL = import.meta.env.VITE_API_CHAT_QUESTION_URL;
const API_TIMEOUT = Number(import.meta.env.VITE_API_TIMEOUT) || 5000;


// Base configuration for Axios
const apiClient = axios.create({
    baseURL: API_BASE_URL,
    timeout: API_TIMEOUT,
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

// Function to send chat message to API
export const sendChatMessage = async (message: string) => {
    try {
      const response = await apiClient.post(API_QUESTION_URL, { question: message });
      return response.data['kwargs']['content'];
    } catch (error) {
      console.error('Error sending chat message:', error);
      throw error;
    }
  };