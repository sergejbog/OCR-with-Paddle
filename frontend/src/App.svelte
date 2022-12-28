<script>
   import { Router, Route } from "svelte-navigator";
   import Examples from "./components/Examples.svelte";
   import NavBar from "./components/NavBar.svelte";
   import { Circle2 } from "svelte-loading-spinners";

   let fileinput;
   let fileName = "No file chosen";
   let selectedOption;
   let resultText,
      resultImage = "https://t3.ftcdn.net/jpg/02/48/42/64/240_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg";
   let showLoading = false;

   const onFileSelected = async (e) => {
      showLoading = true;
      let image = fileinput.files[0];
      let reader = new FileReader();
      let formData = new FormData();
      formData.append("file", image);
      formData.append("language", selectedOption);
      reader.readAsDataURL(image);
      console.log(image);

      let res = await fetch("http://127.0.0.1:5000/", {
         method: "POST",
         body: formData,
      });
      let responseJson = await res.json();
      console.log(responseJson);
      resultText = responseJson["resultString"];
      resultImage = "data:image/png;base64," + responseJson["image"];
      showLoading = false;
   };
</script>

<main>
   <Router>
      <NavBar />
      <Route path="/examples" component={Examples} />
      <Route path="/">
         <div id="home">
            <h1>Optical Character Recognition</h1>
            <hr />
            <h2 class="upper_h2">IMAGE TO TEXT CONVERTER - OCR ONLINE</h2>
            <p>
               Optical Character Recognition allows you to extract text from any image. <br /> This application is using the PaddleOCR suite, which is a set of tools based on neural networks and machine
               learning alghoritms.
            </p>
            <hr />
            <div class="board">
               <div class="upload_image_with_animation">
                  <div class="step_one steps">
                     <h3><span class="bold">Step 1:</span> <br />Upload an image</h3>
                     <!-- svelte-ignore a11y-click-events-have-key-events -->
                     <div
                        class="img_div"
                        on:click={() => {
                           fileinput.click();
                        }}
                     >
                        <img class="upload" src="https://static.thenounproject.com/png/625182-200.png" alt="" />
                     </div>
                     <p class="filename">{fileName}</p>
                  </div>

                  <div class="step_two steps">
                     <h3><span class="bold">Step 2:</span> <br />Select Language</h3>
                     <div class="selection_div">
                        <select name="language" bind:value={selectedOption} id="language">
                           <option value="en">English</option>
                           <option value="ch">Chinese</option>
                           <option value="fr">French</option>
                           <option value="german">German</option>
                           <option value="japan">Japanese</option>
                           <option value="korean">Korean</option>
                        </select>
                     </div>
                     <div class="empty_div" />
                  </div>

                  <div class="step_three steps">
                     <h3><span class="bold">Step 3:</span> <br /> Convert Image</h3>
                     <div class="convert_div">
                        <button on:click={(e) => onFileSelected(e)}>Convert</button>
                     </div>
                     <div class="empty_div" />
                  </div>

                  <input
                     style="display:none"
                     on:change={(e) => {
                        fileName = fileinput.files[0] ? fileinput.files[0].name : "No file chosen";
                     }}
                     type="file"
                     accept=".jpg, .jpeg, .png"
                     bind:this={fileinput}
                  />
               </div>
               <div class="result">
                  <div class="result_inner">
                     <h2>Result Text</h2>
                     <textarea bind:value={resultText} name="result_area" id="result_area" cols="30" rows="10" />
                  </div>
               </div>
            </div>
            <hr />
            <div class="animation">
               {#if showLoading}
                  <Circle2 size="30" unit="px" />
               {/if}
            </div>

            <div class="result_image">
               <h2>Result Image</h2>
               <h3>Format: Line - Probability</h3>
               <div class="result_photo">
                  <img src={resultImage} alt="" />
               </div>
            </div>
         </div>
      </Route>
   </Router>
</main>

<style>
   .upload {
      display: flex;
      height: 50px;
      width: 50px;
   }

   .result_photo {
      margin-top: 20px;
   }

   .bold {
      font-weight: 800;
   }

   h1 {
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 30px;
   }

   h2 {
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 20px;
      /* margin-top: 20px; */
      color: #4682b4;
   }

   #home {
      padding: 50px;
   }

   hr {
      margin-top: 15px;
      width: 100%;
      height: 1px;
      background-color: #4682b4;
      font: bold;
   }

   p {
      font-family: "Lato", sans-serif;
      font-size: 15px;
      margin-top: 20px;
      color: #63676a;
   }

   .upload-image {
      display: flex;
   }

   h3 {
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 15px;
      color: #4682b4;
      display: inline-block;
      height: 40px;
   }

   .img_div {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100px;
      width: 100px;
      border: 1px solid #4682b4;
      border-radius: 5px;
      margin-top: 20px;
      cursor: pointer;
   }

   .selection_div {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100px;
      width: 150px;
      border-radius: 5px;
      margin-top: 20px;
   }

   .step_one {
      display: flex;
      flex-direction: column;
      align-items: center;
   }

   .step_two {
      display: flex;
      flex-direction: column;
      align-items: center;
   }

   .step_three {
      min-width: 33%;
   }

   .steps {
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 33%;
   }

   select {
      width: 200px;
      height: 30px;
      border-radius: 5px;
      border: 1px solid #4682b4;
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 15px;
      color: #4682b4;
   }

   .convert_div {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100px;
      width: 100px;
      border-radius: 5px;
      margin-top: 20px;
   }

   button {
      width: 100px;
      height: 30px;
      border-radius: 5px;
      border: 1px solid #4682b4;
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 15px;
      color: #4682b4;
      background-color: white;
      cursor: pointer;
      transition: all 0.2s;
   }

   button:hover {
      background-color: #4682b4;
      color: white;
   }

   .board {
      display: flex;
      margin-top: 20px;
      width: 100%;
      align-items: center;
   }

   .result {
      display: flex;
      align-items: center;
      justify-content: space-around;
      /* margin-left: 100px; */
      width: 100%;
   }

   .result_inner {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;
      border-left: 1px solid #4682b4;
      padding-left: 50px;
      width: 100%;
   }

   textarea {
      margin-top: 20px;
      width: 500px;
      height: 200px;
      border-radius: 5px;
      border: 1px solid #4682b4;
      font-family: "Lato", sans-serif;
      font-weight: bold;
      font-size: 15px;
      color: #4682b4;
      padding: 10px;
      margin-bottom: 10px;
   }

   .result_image {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;
      margin-top: 40px;
   }

   .upper_h2 {
      margin-top: 20px;
   }

   .upload_image_with_animation {
      display: flex;
      align-items: center;
      width: 100%;
   }

   .filename {
      text-align: center;
   }

   .empty_div {
      margin-top: 40px;
   }

   .animation {
      margin-top: 10px;
      height: 30px;
      width: 100%;
      display: flex;
      justify-content: center;
   }
</style>
