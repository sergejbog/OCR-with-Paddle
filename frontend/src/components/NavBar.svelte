<script>
   import { Link } from "svelte-navigator";
</script>

<nav>
   <Link to="/" class="nav_item">Home</Link>
   <Link to="/examples" class="nav_item">Examples</Link>
</nav>

<style>
   :global(.nav_item) {
      height: 50px;
      width: 200px;
      justify-content: center;
      align-items: center;
      text-decoration: none;
      color: white;
      display: flex;
      font-weight: bold;
      font-family: "Lato", sans-serif;
   }

   :global(.nav_item:hover) {
      background-color: #05365e;
   }

   nav {
      display: flex;
      height: 50px;
      width: 100%;
      background-color: #4682b4;
   }
</style>
