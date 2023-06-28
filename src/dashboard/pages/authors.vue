<template>
     <section class="section" style="margin-top: 3%;">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">

                        <b-form-input v-model="search" name="search" placeholder="Search Author by Name"></b-form-input>
                        <b-button v-b-modal.modal-1>Add Author</b-button>
                        <br>
                        <b-table striped hover :items="filteredItems" :fields="fields" stacked="md" show-empty small>
                    
                            <template v-slot:cell(actions)="{ item }">
                                 <span><b-btn v-b-modal.modal-2 @click="editAuthor(item.id)">Edit</b-btn></span>
                                 <!-- <span><b-btn v-b-modal.modal-2>Delete</b-btn></span> -->
                            </template>

                            

                        </b-table>

                         <b-modal id="modal-1" title="Create New Author">
                            <b-form @submit="saveAuthor">
                                  <b-form-group
                                        id="input-group-1"
                                        label="Author Name:"
                                        label-for="input-1">

                                        <b-form-input
                                            id="input-1"
                                            v-model="name"
                                            type="text"
                                            required>
                                        </b-form-input>
                                   </b-form-group>

                                    <!-- <b-form-group
                                            id="input-group-1"
                                            label="Number of Books:"
                                            label-for="input-1">

                                            <b-form-input
                                                id="input-1"
                                                v-model="number_of_books"
                                                type="text"
                                                required>
                                            </b-form-input>
                                    </b-form-group> -->


                               <b-button type="submit" variant="primary">Submit</b-button>
                            </b-form>    
                         </b-modal>

                         <b-modal id="modal-2" title="Edit Author">                             
                                 <b-form @submit="updateAuthor">
                                      <!-- <b-form-input type="text" v-model="id"></b-form-input>   -->
                                      <b-form-group
                                            id="input-group-1"
                                            label="Author Name:"
                                            label-for="input-1">

                                            <b-form-input
                                                id="input-1"
                                                v-model="name"
                                                type="text"
                                                required>
                                            </b-form-input>
                                       </b-form-group>

                                       <!-- <b-form-group
                                                id="input-group-1"
                                                label="Number of Books:"
                                                label-for="input-1">

                                                <b-form-input
                                                    id="input-1"
                                                    v-model="number_of_books"
                                                    type="text"
                                                    required>
                                                </b-form-input>
                                        </b-form-group> -->


                                   <b-button type="submit" variant="primary">Submit</b-button>
                                </b-form>   
                         </b-modal>
                    </div>
                </div>
            </div>
    </section>
</template>

<script>
import axios from 'axios'
import AuthorService from "../services/AuthorService";

export default{
      data() {
        return {
            search: '',
            id: null,
            name: null,
            number_of_books:null,
            error: null,
            fields: [{key: 'id',sortable: true}, { key: 'name', sortable: false }, { key: "number_of_books" },{ key: "actions" }],
            authors:[{id:"1",name:"John"}, { id: "2",name:"Catherine" }]
        }
    },

    async created(){
        this.getAuthors();
    },
    computed: {
        filteredItems() {
            if (this.search.trim() === '') {
                return this.authors;
            }
            const searchTerm = this.search.toLowerCase();
            return this.authors.filter(item => item.name.toLowerCase().includes(searchTerm));
        }
    },
    watch:{
        search(newvalue, oldvalue){
            console.log('Search Text Changed:', newvalue);
        }
    },

    methods: {

     getAuthors(){
            AuthorService.fetchAuthor().then((response) => {
                     console.log(process.env.BASE_URL);
                     console.log(response.data);
                     this.authors = response.data;
                     //this.$toast.success(response, { icon: "done" });
                }).catch((response) => {
                    console.log(response);
                    this.$toast.success(response, { icon: "Failed" });
                });
     },   
     saveAuthor() {
         event.preventDefault();
         //this.resetAuthor();
         console.log("Saving Author ..");    
          var data = { "name": this.name, "number_of_books": this.number_of_books, };
          AuthorService.saveAuthor(data).then((response) => {
                console.log(response.data);
                this.resetAuthor();
                this.getAuthors();
                this.$toast.success("Added new author succesfully", { icon: "done" });
            }).catch((response) => {
                console.log(response.data);
                this.$toast.success(response.data, { icon: "Failed" });
            });   
       
     },
     editAuthor(value) {
        const result = this.authors.find((item) => item.id == value);
           this.id = result.id;
           this.name = result.name;
           this.number_of_books = result.number_of_books;
     },
      updateAuthor() {
           event.preventDefault()
           console.log("updating ..");

            var data = { "id":this.id,"name": this.name, "number_of_books": this.number_of_books, };
            AuthorService.updateAuthor(data,this.id).then((response) => {
                console.log(response.data);
                this.resetAuthor();
                this.getAuthors();
                this.$toast.success("Updated author succesfully", { icon: "done" });
            }).catch((response) => {
                console.log(response.data);
                this.$toast.success(response.data, { icon: "Failed" });
            });

      },

      resetAuthor() {
            this.id = null;
            this.name = null;
            this.number_of_books = null;
        },
    }
}

</script>