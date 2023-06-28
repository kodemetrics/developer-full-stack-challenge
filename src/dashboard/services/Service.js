import { createService } from 'vue-axios';
import { axios } from '~/plugins/axios';

const service = createService({
  axios,
  baseURL: axios.defaults.baseURL,
});

export default service;