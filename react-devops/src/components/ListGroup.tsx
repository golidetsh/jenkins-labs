function ListGroup() {

    let posts = ["Top 10 Recipes", "EPL Diaries", "Tokyo Drift Story", "Johannesburg By Night"]; 
    //posts = [];

  return (
    <>
      <h1>MyList</h1>
      {posts.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {posts.map((post) => (
          <li
            className="list-group-item"
            key={post}
            onClick={() => console.log("Clicked")}
          >
            {post}
          </li>
        ))}
      </ul>
    </>
  );

}

export default ListGroup;