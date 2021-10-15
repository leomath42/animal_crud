import axios from 'axios'

export const BASE_URL = process.env.REACT_APP_BACKEND_URL ?? 'http://localhost:5000';
axios.defaults.baseURL = BASE_URL;
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';