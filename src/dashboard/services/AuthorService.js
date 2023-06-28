import axios from 'axios';
import {state} from '~/store/index';

const BASE_URL = process.env.BASEURL + "authors/"
const headers =  {
        'Authorization':'Bearer '+ state().token,
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=utf-8'
};
class AuthorService{

    saveAuthor(author){
        return axios.post(BASE_URL,author,{headers:headers});
    }
    fetchAuthor(){
        console.log(process.env.BASEURL);
        return axios.get(BASE_URL,{headers:headers});
    }
    updateAuthor(author,id){
         return axios.put(BASE_URL+id,author,{headers:headers});
    }
    deteteAuthor(author,id){
         return axios.delete(BASE_URL+id,author,{headers:headers});
    }

}
export default new AuthorService();

