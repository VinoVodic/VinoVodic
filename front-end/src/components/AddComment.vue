<template>
  <div class="card">
    <div class="row">
      <div class="col-10">
        <div class="comment-box ml-2">
          <form>
            <h4>Додајте коментар и оцена</h4>
            <div class="rating">
              <input type="radio" name="rating" value="5" id="5"><label for="5">☆</label>
              <input type="radio" name="rating" value="4" id="4"><label for="4">☆</label>
              <input type="radio" name="rating" value="3" id="3"><label for="3">☆</label>
              <input type="radio" name="rating" value="2" id="2"><label for="2">☆</label>
              <input type="radio" name="rating" value="1" id="1"><label for="1">☆</label>
            </div>
            <div class="comment-area">
              <textarea class="form-control" placeholder="Додајте коментар..." rows="4" v-model="comment"></textarea>
            </div>
            <div class="comment-btns mt-2">
              <div class="row">
                <div class="col-6">
                  <button class="btn send btn-sm" type="submit" @click.prevent="sendReview">Зачувај<i class="fa fa-long-arrow-right ml-1"></i></button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="showErrorMessage" class="error-message">
    {{ this.errorMessage }}
  </div>
</template>

<script>
import {store} from "@/store/store";
import router from "@/router";

export default {
  name: "AddComment",
  data() {
    return {
      showErrorMessage: false,
      errorMessage: "",
    }
  },
  computed: {
    selectedWinery() {
      const storedWinery = sessionStorage.getItem("selectedWinery");
      return JSON.parse(storedWinery);
    },
  },
  methods: {
    async sendReview() {
      if(sessionStorage.getItem("loggedIn") === "false" || sessionStorage.getItem("loggedIn") === null) {
        await router.push("/login")
        return;
      }
      const selectedRating = this.getSelectedRating();

      if(selectedRating === null) {
        this.showErrorMessage = true
        this.errorMessage = "Please fill out all fields"
        setTimeout(() => {
          this.showErrorMessage = false;
        }, 3000);
      }

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + sessionStorage.getItem("access")
        },
        body: JSON.stringify({
          "rating": selectedRating,
          "winery_id": this.selectedWinery.id,
          "comment": this.comment ?? ""
        })
      };

      const response = await fetch(store.api_url + "/profiles/reviews/", requestOptions);

      if(response.status === 201) {
        await router.go(0)
      }
    },
    getSelectedRating() {
      const checkedRating = document.querySelector('.rating input:checked');
      return checkedRating ? checkedRating.value : null;
    }
  }
}
</script>

<style scoped>
  .card {
    background-color: var(--secondary-color);
    padding: 1rem;
    width:95%;
    background-clip: border-box;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  .comment-box{
    padding: 1rem 3rem;
  }

  .comment-area textarea{
    width: 100%;
    resize: none;
    border: 1px solid #ad9f9f;
  }


  .form-control:focus {
    color: #495057;
    box-shadow: 0 0 0 1px var(--primary-color) !important;
  }

  .send {
    color: #fff;
    background-color: var(--primary-color);
    border-color: var(--primary-color);
  }

  .send:hover {
    color: #fff;
    background-color: var(--primary-color);
    border-color: var(--primary-color);
  }

  .rating {
    display: flex;
    margin-top: -10px;
    flex-direction: row-reverse;
    margin-left: -4px;
    float: left;
  }

  .rating>input {
    display: none
  }

  .rating>label {
    position: relative;
    width: 19px;
    font-size: 25px;
    color: var(--primary-color);
    cursor: pointer;
  }

  .rating>label::before {
    content: "\2605";
    position: absolute;
    opacity: 0
  }

  .rating>label:hover:before,
  .rating>label:hover~label:before {
    opacity: 1 !important
  }

  .rating>input:checked~label:before {
    opacity: 1
  }

  .rating:hover>input:checked~label:before {
    opacity: 0.4
  }

  .error-message {
    position: fixed;
    top: 56.5%;
    left: 38%;
    transform: translateX(-50%);
    background-color: var(--primary-color);
    color: white;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
</style>