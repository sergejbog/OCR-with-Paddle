<script>
   import { Circle2 } from "svelte-loading-spinners";

   let pickedImage = "https://t3.ftcdn.net/jpg/02/48/42/64/240_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg";
   let showLoading = false;
   let resultText, resultImage;
   let photos = ["barcode.jpg", "captcha.jpg", "handwriting.jpg", "ICR5.jpg", "mobile_photo_2.jpg", "mobile_photo.jpg", "plaid_c150.jpg", "stock.jpg"];
   const startExample = async (e) => {
      showLoading = true;
      let image = e.target.previousElementSibling.src;

      let imgBlob = await fetch(image).then((r) => r.blob());
      let formData = new FormData();

      formData.append("file", imgBlob);
      formData.append("language", "en");
      let res = await fetch("http://127.0.0.1:5000/", {
         method: "POST",
         body: formData,
      });
      let responseJson = await res.json();
      console.log(responseJson);
      resultText = responseJson["resultString"].split("\n").join("  ");
      resultImage = "data:image/png;base64," + responseJson["image"];
      pickedImage = image;
      showLoading = false;
   };
</script>

<section>
   <h1>Here are some examples using different photos</h1>
   <hr class="normalLine" />
   <div class="animation">
      {#if showLoading}
         <Circle2 size="30" unit="px" />
      {/if}
   </div>
   <div class="examples_div">
      {#each photos as photo}
         <div class="example">
            <img class="example_img" src={photo} alt="" />
            <button class="start_btn" on:click={startExample}>Start</button>
         </div>
      {/each}
   </div>
   <hr class="normalLine" />
   <div class="results">
      <textarea bind:value={resultText} name="resultText" id="resultText" cols="30" rows="10" />
   </div>
   <div class="result_img">
      <img src={resultImage} alt="" />
   </div>
</section>

<style>
   section {
      padding: 50px;
   }

   h1 {
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 30px;
   }

   .normalLine {
      margin-top: 15px;
      width: 100%;
      height: 1px;
      background-color: #4682b4;
      font: bold;
   }

   .examples_div {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 50px;
   }

   .example {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin: 20px;
   }

   .example_img {
      width: 200px;
      height: 200px;
      object-fit: cover;
   }

   .results {
      display: flex;
      justify-content: space-around;
      margin-top: 50px;
   }

   textarea {
      width: 100%;
      height: 100%;
      resize: none;
      font-family: "Lato", sans-serif;
      font-size: 20px;
      font-weight: bold;
      padding: 10px;
      margin-bottom: 40px;
   }

   .start_btn {
      width: 100px;
      height: 50px;
      background-color: #4682b4;
      color: white;
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 20px;
      border: none;
      border-radius: 5px;
      margin-top: 10px;
      cursor: pointer;
      transition: all 0.15s;
   }

   .start_btn:hover {
      background-color: #05365e;
   }

   .animation {
      margin-top: 10px;
      height: 30px;
      width: 100%;
      display: flex;
      justify-content: center;
   }
</style>
