function ListGroup() {

    let posts = ["Top 10 Recipes", "EPL Diaries", "Tokyo Drift Story", "Johannesburg By Night"]; 

  return (
    <>
      <h1>MyList</h1>
      <ul className="list-group">
        <li className="list-group-item">An item</li>
        <li className="list-group-item">A second item</li>
      </ul>
    </>
  );

}

export default ListGroup;