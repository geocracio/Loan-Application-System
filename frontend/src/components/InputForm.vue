<template>
  <form>
    <div class="title">Loan Approver</div>
    <div class="subtitle">Apply for your next credit!</div>
    <button @click="checkAPI">click me</button>
    <div class="row">
      <div class="input-container ic1">
        <input class="input" type="text" required placeholder=" " v-model="income"/>
        <div class="cut"></div>
        <label class="placeholder">Income</label>
      </div>
      <div class="input-container ic1">
        <input class="input" type="text" required placeholder=" " v-model="age"/>
        <div class="cut"></div>
        <label class="placeholder">Age</label>
      </div>
    </div>
    <div class="row">
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="experience"/>
        <div class="cut"></div>
        <label class="placeholder">Experience</label>
      </div>
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="maritalStatus"/>
        <div class="cut"></div>
        <label class="placeholder">Marital Status</label>
      </div>
    </div>
    <div class="row">
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="houseOwnership"/>
        <div class="cut"></div>
        <label class="placeholder">House Ownership</label>
      </div>
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="carOwnership"/>
        <div class="cut"></div>
        <label class="placeholder">Car Ownership</label>
      </div>
    </div>
    <div class="row">
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="profession"/>
        <div class="cut"></div>
        <label class="placeholder">Profession</label>
      </div>
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="currentJobYears"/>
        <div class="cut"></div>
        <label class="placeholder">Current Job Years</label>
      </div>
    </div>
    <div class="row">
      <div class="input-container ic2">
        <input class="input" type="text" required placeholder=" " v-model="currentHouseYears"/>
        <div class="cut"></div>
        <label class="placeholder">Current House Years</label>
      </div>
    </div>
    <button @click="submitForm" class="submit">Submit</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      income: null,
      age: null,
      experience: null,
      maritalStatus: '',
      houseOwnership: '',
      carOwnership: '',
      profession: '',
      currentJobYears: null,
      currentHouseYears: null,
      predictions: [],
    }
  },
  methods: {
    async checkAPI() {
      const postData = {
        income: 0,
        age: 0,
        experience: 0,
        maritalStatus: "string",
        houseOwnership: "string",
        carOwnership: "string",
        profession: "string",
        currentJobYears: 0,
        currentHouseYear: 0
      };
      console.log(postData)
      axios.post('http://127.0.0.1:8000/predict', postData)
        .then(response => {
          this.predictions = response.data.predictions;
          console.log(response)
        })
        .catch(error => {
          console.error(error);
        });
    },
    async submitForm() {
      const postData = {
        income: this.income,
        age: this.age,
        experience: this.experience,
        maritalStatus: this.maritalStatus,
        houseOwnership: this.houseOwnership,
        carOwnership: this.carOwnership,
        profession: this.profession,
        currentJobYears: this.currentJobYears,
        currentHouseYear: this.currentHouseYears,
      };
      console.log(postData)
      axios.post('http://127.0.0.1:8000/predict', postData)
        .then(response => {
          this.predictions = response.data.predictions;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
p {
  color: #ffffff;
}

form {
  background-color: #15172b;
  border-radius: 20px;
  box-sizing: border-box;
  padding: 20px;
  width: 100%;
}

.title {
  color: #eee;
  font-family: sans-serif;
  font-size: 36px;
  font-weight: 600;
  margin-top: 30px;
  text-align: center;
}

.subtitle {
  color: #eee;
  font-family: sans-serif;
  font-size: 16px;
  font-weight: 600;
  margin-top: 10px;
  text-align: center;
}

.input-container {
  height: 50px;
  position: relative;
  margin: 0px 25px;
  width: 40%;
}

.ic1 {
  margin-top: 40px;
}

.ic2 {
  margin-top: 30px;
}

.input {
  background-color: #303245;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  font-size: 18px;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 100%;
}

.cut {
  background-color: #15172b;
  border-radius: 10px;
  height: 20px;
  left: 20px;
  position: absolute;
  top: -20px;
  transform: translateY(0);
  transition: transform 200ms;
  width: 76px;
}

.cut-short {
  width: 50px;
}

.input:focus ~ .cut,
.input:not(:placeholder-shown) ~ .cut {
  transform: translateY(8px);
}

.placeholder {
  color: #65657b;
  font-family: sans-serif;
  left: 20px;
  line-height: 14px;
  pointer-events: none;
  position: absolute;
  transform-origin: 0 50%;
  transition: transform 200ms, color 200ms;
  top: 20px;
}

.input:focus ~ .placeholder,
.input:not(:placeholder-shown) ~ .placeholder {
  transform: translateY(-30px) translateX(10px) scale(0.75);
}

.input:not(:placeholder-shown) ~ .placeholder {
  color: #808097;
}

.input:focus ~ .placeholder {
  color: #dc2f55;
}

.submit {
  background-color: #08d;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  color: #eee;
  cursor: pointer;
  font-size: 18px;
  height: 50px;
  margin-top: 38px;
  text-align: center;
  width: 100%;
}

.submit:active {
  background-color: #06b;
}

.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

</style>