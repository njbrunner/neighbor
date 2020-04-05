<template>
  <div>
    <v-dialog v-model="dialog" persistent max-width="800px">
      <v-row
        :align="center"
        :justify="center"
      >
        <v-col>
          <button class="button-dialog">I could use help</button>
        </v-col>
        <v-col>
          <button class="button-dialog">I am willing to help</button>
        </v-col>
      </v-row>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "ModeSelection",
  props: {
    role: Boolean
  },
  computed: {
    dialog() {
      return !this.role;
    }
  }
};
</script>

<style>

.button-dialog {
  border: solid red 1px;
  width: 100%;
  min-height: 300px;
}
</style>
