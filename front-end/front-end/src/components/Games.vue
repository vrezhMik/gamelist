<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library 🕹
          </h1>
          <hr />
          <br />
          <!-- TODO: add timing to hide the message -->
          <b-alert variant="success" v-if="showMessage" show>{{
            message
          }}</b-alert>
          <button type="button" class="btn btn-success" v-b-modal.game-modal>
            Add Game
          </button>
          <br />
          <br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played?</th>
                <th scope="col">Actiosn</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, id) in games" :key="id">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">yes</span>
                  <span v-else>no</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      class="btn btn-info"
                      type="button"
                      v-b-modal.game-update-modal
                      @click="editGame(game)"
                    >
                      Update
                    </button>
                    <button
                      class="btn btn-danger"
                      type="button"
                      @click="deleteGame(game)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy; All rights Reserved 2023
          </footer>
        </div>
      </div>
      <!-- Modal 1  -->
      <b-modal
        ref="addGameModel"
        id="game-modal"
        title="Add a new game"
        hide-backgrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              required
              v-model="addGameForm.title"
              placeholder="Enter Game"
            />
          </b-form-group>
          <b-form-group
            id="form-genre-group"
            label="Genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              required
              v-model="addGameForm.genre"
              placeholder="Enter Genre"
            />
          </b-form-group>
          <b-form-group>
            <b-form-checkbox-group
              v-model="addGameForm.played"
              id="form-checks"
            >
              <b-form-checkbox value="true">Played?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="submit" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>

      <!-- Modal 2 -->
      <b-modal
        ref="editGameModel"
        id="game-update-modal"
        title="Update"
        hide-backgrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group
            id="form-title-edit-group"
            label="Title:"
            label-for="form-title-edit-input"
          >
            <b-form-input
              id="form-title-edit-input"
              type="text"
              required
              v-model="editForm.title"
              placeholder="Enter Game"
            />
          </b-form-group>
          <b-form-group
            id="form-genre-edit-group"
            label="Genre:"
            label-for="form-genre-edit-input"
          >
            <b-form-input
              id="form-genre-edit-input"
              type="text"
              required
              v-model="editForm.genre"
              placeholder="Enter Genre"
            />
          </b-form-group>
          <b-form-group>
            <b-form-checkbox-group v-model="editForm.played" id="form-checks">
              <b-form-checkbox value="true">Played?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="outline-info">Update</b-button>
          <b-button type="submit" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "GamesComp",
  data() {
    return {
      games: [],
      showMessage: false,
      addGameForm: {
        title: "",
        genre: "",
        played: [],
      },
      editForm: {
        id: "",
        title: "",
        genre: "",
        played: [],
      },
    };
  },
  message: "",
  methods: {
    getGames() {
      const path = "http://127.0.0.1:5000/games";
      axios
        .get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((err) => console.log(err));
    },
    addGame(payload) {
      const path = "http://127.0.0.1:5000/games";
      axios
        .post(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game added successfully";
          this.showMessage = true;
        })
        .catch((err) => console.log(err));
    },
    updateGame(payload, id) {
      const path = `http://127.0.0.1:5000/games/${id}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game updated successfully";
          this.showMessage = true;
        })
        .catch((err) => console.log(err));
    },
    removeGame(id) {
      const path = `http://127.0.0.1:5000/games/${id}`;
      axios
        .delete(path)
        .then(() => {
          this.getGames();
          this.message = "Game deleted successfully";
          this.showMessage = true;
        })
        .catch((err) => console.log(err));
    },
    editGame(game) {
      this.editForm = game;
    },
    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.played = [];
      this.editForm.id = "";
      this.editForm.title = "";
      this.editForm.genre = "";
      this.editForm.played = [];
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addGameModel.hide();
      let played = false;
      if (this.addGameForm.played[0]) played = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played,
      };
      this.addGame(payload);
      this.initForm();
    },
    onReset(e) {
      e.preventDefault();
      this.$ref.addGameModel.hide();
      this.initForm();
      this.getGames();
    },
    deleteGame(game) {
      this.removeGame(game.id);
    },
    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.editGameModel.hide();
      let played = false;
      if (this.editForm.played[0]) played = true;
      const payload = {
        title: this.editGameForm.title,
        genre: this.editGameForm.genre,
        played,
      };
      this.updateGame(payload, this.editForm.id);
    },
    onResetUpdate(e) {
      e.preventDefault();
      this.$ref.editGameModel.hide();
      this.initForm();
      this.getGames();
    },
  },
  created() {
    this.getGames();
  },
};
</script>
