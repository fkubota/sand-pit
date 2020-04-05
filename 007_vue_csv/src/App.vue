<template>
  <div>
    <h1>CSVインポート</h1>
    <input @change="fileChange" type="file" id="file_input_expense" name="file_input_expense">
    <v-data-table :headers="headers" :items="workers" class="elevation-1">
      <template slot="items" slot-scope="props">
        <td class="text-xs-right">{{ props.item.code }}</td>
        <td class="text-xs-right">{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.workerType }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      headers: [
        {
          text: "Code",
          align: "left",
          sortable: false,
          value: "code"
        },
        { text: "Name", align: "left", value: "name" },
        { text: "WorkerType", align: "left", value: "workerType" }
      ],
      workers: []
    };
  },
  methods: {
    fileChange: function(e) {
      const file = e.target.files[0];
      const reader = new FileReader();
      const workers = [];

      const loadFunc = () => {
        const lines = reader.result.split("\n");
        lines.forEach(element => {
          const workerData = element.split(",");
          if (workerData.length != 3) return;
          const worker = {
            code: workerData[0],
            name: workerData[1],
            workerType: workerData[2]
          };
          workers.push(worker);
        });
        this.workers = workers;
      };

      reader.onload = loadFunc;

      reader.readAsBinaryString(file);
    }
  }
};
</script>