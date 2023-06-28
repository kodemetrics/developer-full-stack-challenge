export default function ({ store, redirect }) {
   console.log(store.state.isLoggedIn);
   console.log(store.state.auth.loggedIn);
  // Check if the user is logged in
    if (store.state.isLoggedIn) {
    //if (store.state.auth.loggedIn) {
      return redirect('/');
    }

}